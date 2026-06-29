def brew_chai(flavour):
    if flavour not in ["mashala", "ginger", "elaichi"]:
        raise ValueError(f"unsupported chai flavour")
    
    print(f"brewing {flavour} chai")

brew_chai("ginger")