# question
# -------------------------------------------------------------------------------------

file_system = {
    'folder1': {
        'subfolder1': {
            'file1': 'content1',
            'file2': 'content2'
        },
        'subfolder2': {
            'file3': 'content3'
        }
    },
    'folder2': {
        'file4': 'content4'
    },
    'file5': 'content5'
}


# output
# -------------------------------------------------------------------------------------

{
    'folder1/subfolder1/file1': 'content1',
    'folder1/subfolder1/file2': 'content2',
    'folder1/subfolder2/file3': 'content3',
    'folder2/file4': 'content4',
    'file5': 'content5'
}


# solution
# -------------------------------------------------------------------------------------

dct = {}
for key1, val1 in file_system.items():
    if isinstance(val1, dict):
        for key2, val2 in val1.items():
            if isinstance(val2, dict):
                for key3, val3 in val2.items():
                    dct[key1 + '/' + key2 + '/' + key3] = val3
            else:
                dct[key1 + '/' + key2] = val2
    else:
        dct[key1] = val1
print(dct)

print()
