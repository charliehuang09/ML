from fastai.vision.all import *
from fastai.vision.widgets import *
path = '/Users/charlie/ML/FastAI/dataset'

dls = ImageDataLoaders.from_folder(path, valid_pct=0.2, item_tfms=RandomResizedCrop(224))
dls.device = torch.device('cpu')
learn = vision_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(5, cbs=[ShowGraphCallback()])

interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()