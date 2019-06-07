tablesql = {

}

def dict2sql(dictIn, tdef=None):
    command_body = "INSERT INTO {} VALUES (\'{}\');"
    commands = []
    global command_body, tabledef
    if not tdef:
        tdef = tablesql
    for tablename in tdef:
        for element in dictIn[tablename["table"]]:
            elements_fields = "\',\'".join(element)
            commands.append(command_body.format(tablename["table"], elements_fields))
    return commands