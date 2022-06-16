def test(args):
    model = nnet.get_model()
    model = DataParallel(model)
    checkpoint_path = utils.get_ckpt_folder(args)
    save_name = os.path.join(checkpoint_path,args.model + '_' + str(args.iteration)+'.pth')
    model.load_state_dict(torch.load(save_name))
    model.to(args.device)
    identity_list = get_lfw_list(args.test_list_path)