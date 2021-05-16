def verify_melli_code(melli_code:str):
    melli_full  = [x for x in melli_code]
    melli_validator_number = int(melli_full[-1])

    melli_index = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    melli_check = melli_full[:len(melli_full)-1]

    validate = sum([index*int(number) for index, number in zip(melli_index, melli_check)])
    returned_validator = validate % 11

    if returned_validator <= 1:
        if (returned_validator == 0) and melli_validator_number == 0:
            return True
        elif (returned_validator == 1) and melli_validator_number == 1:
            return True
        else : return False
    elif (11 - returned_validator) ==  melli_validator_number:
        return True

    else : return False

