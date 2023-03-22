import importlib
import omegaconf
import albumentations as A
from omegaconf import DictConfig

from typing import Any

def load_obj(obj_path: str, default_obj_path: str = "") -> Any:
    """
    Extract an object from a given path.
        Args:
            obj_path: Path to an object to be extracted, including the object name.
            default_obj_path: Default object path.
        Returns:
            Extracted object.
        Raises:
            AttributeError: When the object does not have the given named attribute.

    Thanks to Erlemar: https://github.com/Erlemar/wheat/blob/cee864462551a68056ae15cf8bfebb3efae79189/src/utils/get_dataset.py
    """
    obj_path_list = obj_path.rsplit(".", 1)
    obj_path = obj_path_list.pop(0) if len(obj_path_list) > 1 else default_obj_path
    obj_name = obj_path_list[0]
    module_obj = importlib.import_module(obj_path)
    if not hasattr(module_obj, obj_name):
        raise AttributeError(f"Object `{obj_name}` cannot be loaded from `{obj_path}`.")
    return getattr(module_obj, obj_name)



def load_augs(cfg: DictConfig) -> A.Compose:
    """
    Load albumentations config and return a the composed transformations.
    Thanks to Erlemar: https://github.com/Erlemar/wheat/blob/cee864462551a68056ae15cf8bfebb3efae79189/src/utils/get_dataset.py

    """
    if "json_cfg" in cfg:
        return A.load(cfg.json_cfg)
    augs = []
    for a in cfg:
        if a["class_name"] == "albumentations.OneOf":
            small_augs = []
            for small_aug in a["params"]:
                params = {
                    k: (v if type(v) != omegaconf.listconfig.ListConfig else tuple(v))
                    for k, v in small_aug["params"].items()
                }
                aug = load_obj(small_aug["class_name"])(**params)
                small_augs.append(aug)
            aug = load_obj(a["class_name"])(small_augs)
            augs.append(aug)

        else:
            params = {
                k: (v if type(v) != omegaconf.listconfig.ListConfig else tuple(v))
                for k, v in a["params"].items()
            }
            aug = load_obj(a["class_name"])(**params)
            augs.append(aug)
    if len(augs) == 1:
        return augs[0]
    else:
        return A.Compose(augs)



if __name__ == "__main__":
    path_to_augmentation = "transformations/cs_distort.yaml"