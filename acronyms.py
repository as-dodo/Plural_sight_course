acronyms = {'LOL': 'laugh out loud',
            'IDK': 'I don\'t know',
            'TBH': 'to be honest'}

acronyms['IMHO'] = 'in my humble opinion'

# definition = acronyms.get('BTW')
#
# if definition:
#     print(definition)
# else:
#     print('Key doesn\'t exist')

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence: ', sentence)
print('translation: ', translation)

sent = 'IDK what happened TBH'
orig_sent = sent.split(' ')
trans_sent_list = []
for elem in orig_sent:
    if elem in acronyms.keys():
        elem = acronyms[elem]
    trans_sent_list.append(elem)
trans_sent = ' '.join(trans_sent_list)

print(sent)
print(trans_sent)
