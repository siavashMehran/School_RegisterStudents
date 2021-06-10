def querryDict_generator(request_POST:dict, **kwargs):
    QD = request_POST.copy()
    for k, v in kwargs.items():
        QD[k] = v
    return QD
