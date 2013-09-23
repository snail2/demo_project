"""
Views.
"""

from django.shortcuts import render

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

#NEW
CODONS = {
    'UUU' : 'Phe',
    'UUC' : 'Phe',
    'UUA' : 'Leu',
    'UUG' : 'Leu',
    
    'UCU' : 'Ser',
    'UCC' : 'Ser',
    'UCA' : 'Ser',
    'UCG' : 'Ser',
    
    'UAU' : 'Tyr',
    'UAC' : 'Tyr',
    'UAA' : '---',
    'UAG' : '---',
    
    'UGU' : 'Cys',
    'UGC' : 'Cys',
    'UGA' : '---',
    'UGG' : 'Trp',


    'CUU' : 'Leu',
    'CUC' : 'Leu',
    'CUA' : 'Leu',
    'CUG' : 'Leu',
    
    'CCU' : 'Pro',
    'CCC' : 'Pro',
    'CCA' : 'Pro',
    'CCG' : 'Pro',
    
    'CAU' : 'His',
    'CAC' : 'His',
    'CAA' : 'Gln',
    'CAG' : 'Gln',
    
    'CGU' : 'Arg',
    'CGC' : 'Arg',
    'CGA' : 'Arg',
    'CGG' : 'Arg',


    'AUU' : 'Ile',
    'AUC' : 'Ile',
    'AUA' : 'Ile',
    'AUG' : 'Met',
    
    'ACU' : 'Thr',
    'ACC' : 'Thr',
    'ACA' : 'Thr',
    'ACG' : 'Thr',
    
    'AAU' : 'Asn',
    'AAC' : 'Asn',
    'AAA' : 'Lys',
    'AAG' : 'Lys',
    
    'AGU' : 'Ser',
    'AGC' : 'Ser',
    'AGA' : 'Arg',
    'AGG' : 'Arg',


    'GUU' : 'Val',
    'GUC' : 'Val',
    'GUA' : 'Val',
    'GUG' : 'Val',
    
    'GCU' : 'Ala',
    'GCC' : 'Ala',
    'GCA' : 'Ala',
    'GCG' : 'Ala',
    
    'GAU' : 'Asp',
    'GAC' : 'Asp',
    'GAA' : 'Glu',
    'GAG' : 'Glu',
    
    'GGU' : 'Gly',
    'GGC' : 'Gly',
    'GGA' : 'Gly',
    'GGG' : 'Gly',
}
#NEW


def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''
        #NEW
        valid = True
        #NEW
        for base in query_string:
            #NEW
            if base not in ['A','C','G','T']:
                valid = False
                break
            #NEW
            reverse_complement += BASE_PAIRING[base]
        context['query_string'] = query_string
        #NEW
        if valid: #do the next lines; else display Error message
        #NEW
            context['reverse_complement'] = reverse_complement
        else:
            context['reverse_complement'] = 'Error: Please only enter A, C, G, and T'
        #Kai was here

    return render(request, 'home.html', context)
