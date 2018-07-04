from data import Channel
from cf_workflow import run as user_cf

def manage():
    #dat to csv
    Channel().process()
    #run cf_workflow
    user_cf()

if __name__ == '__main__':
    manage()
