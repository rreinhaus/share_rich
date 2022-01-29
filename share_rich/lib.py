def try_me(mood):
    if mood =='happy':
        return 'Great, to hear that, have a lovely day'
    elif mood == 'tired':
        return 'Lets meet tomorrow? I think you should go to bed!'
    return 'Thanks for sharing have a lovely day!'

if __name__ == "__main__":
    moody = try_me('tired')
    print(moody)