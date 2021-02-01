from loader import data_loader
import csv
import torch
import os
from pytorch_lightning.metrics import F1

def save_model(model, optimizer, scheduler) : 
    model_cpu = model.to('cpu')
    state = {
        'model' : model_cpu.state_dict(),
        'optimizer' : optimizer.state_dict(),
        'scheduler' : scheduler.state_dict()
    }
    if not(os.path.isdir('./saved_model')) : os.mkdir('./saved_model')
    torch.save(state, './saved_model/saved_model.pth')


def train_val():   
    
    '''
    # define or import model 
    model = model.resnet()

    # define loss fc
    loss_fn = nn.BCELoss()

    # define optimizer
    optimizer = optim.Adam(
        [param for param in model.parameters() if param.requires_grad], 
        lr = 0.001, weight_decay=1e-4)

    # define scheduler
    scheduler = StepLR(optimizer, step_size = 5, gamma =0.5)        
    '''

    train_loader = data_loader(phase='train', batch_size=1)
    
    epoch = 100
    for idx, item in range(0, epoch) :
        lst_out = []
        lst_label = []
        for image, label in enumerate(train_loader):
            '''
            ### Example ### 
            
            out = model(image)
            lst_out+=out.item()
            lst_label +=label

            
            ### Calculate loss, backward loss and optimizer step ###
            loss = loss_fn(out, label)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            '''


            ### Sample ###
            lst_out += [0,1,2,3,4]
            lst_label += [0,1,2,3,4]
            ###########

        #scheduler.step()
    # save_model(model, optimizer, scheduler)

    f1 = F1(num_classes=5, average = 'macro')
    print(lst_out, lst_label)
    print(f1(torch.tensor(lst_out), torch.tensor(lst_label)))

def test() :
    dic_label = {0:'Wake', 1:'REM', 2:'N1', 3:'N2', 4:'N3'}
    test_loader = data_loader(phase='test', batch_size= 1)
    f1 = open('./test_result.csv', 'w', encoding ='utf-8-sig', newline='')
    wr = csv.writer(f1)
    lst_out = []
    lst_label = []
    ct = 0

    '''
    ### Example ### 
    
    # define or import model 
    model = model.resnet()

    # load model
    state = torch.load('./saved_model/saved_model.pth')
    model.load_state_dict(state['model'])
    '''

    for image, _ in enumerate(test_loader):
        # out = model(image)
        # lst_out+=out.item()
        # lst_label +=label

        #example
        lst_out = [0,1,2,3,4]
        for idx, item in enumerate(lst_out) :
            wr.writerows([[dic_label[item]]])

if __name__ == "__main__":

    # train_val()
    # test()