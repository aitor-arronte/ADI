from utils.dataloader import get_data
from models.crnn import CRNN
from models.residual import ResidualLSTM, Resblock
from models import train
import torch

train_data, test_data = get_data()
#model = CRNN()
model = ResidualLSTM(Resblock, [2])
if torch.cuda.is_available():
    device = torch.device('cuda:0')
else:
    device = torch.device('cpu')
model.to(device)
train.train_model(model, train_data)
train.test_model(model, test_data)