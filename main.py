import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
session = fo.launch_app(dataset, port=5151)





dataset2 = fo.load_zoo_dataset("animals")
session = fo.launch_app(dataset2, port=5052)


session.wait()
