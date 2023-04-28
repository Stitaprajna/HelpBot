import gpt_2_simple as gpt2

def train(model):
    #### Initilize the pre-trained model
    sees = gpt2.start_tf_sess()
    file_name = 'train_phase_1.txt'

    ###### Training the loaded model ######
    gpt2.finetune(sees,
                dataset=file_name,
                steps=10000,
                model_name='124M',
                restore_from='fresh',
                run_name='run1',
                print_every=10,
                sample_every=10,
                save_every=10,
                checkpoint_dir='new_checkpoint'
                
    )

#### Train ####
train()