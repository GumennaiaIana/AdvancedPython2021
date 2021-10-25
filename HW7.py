# -*- coding: utf-8 -*-

import random
class NA:
    def __init__(self, seq):
        self.seq = seq
        
    def correct(self, seq): 
        if seq is None:
            return True
        for ch in seq:
            if not (ch in self._dict):
                return False
        return True
    
    def complementary(self):
        new_seq = ''
        for ch in self.seq:
            new_seq = new_seq + self._dict[ch]
        return new_seq
    
    def __mul__(self, other):
        new_seq = [random.choice(pair) for pair in list(zip(self.seq, other.seq))]  
        new_seq = ''.join(new_seq)
        if len(self.seq) > len(other.seq):
            new_seq += self.seq[-(len(self.seq) - len(other.seq)):]
        elif len(other.seq) > len(self.seq):
            new_seq += self.seq[-(len(other.seq) - len(self.seq)):]
        return self.__class__(seq=new_seq)
    
    def __getitem__(self, item):
        raise NotImplementedError
        
    def __add__(self, other):
        raise NotImplementedError

class RNA(NA):
    def __init__(self, seq):
        self._dict = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}
        if self.correct(seq) == True:
            super().__init__(seq=seq)
        else:
            raise Exception

    def __getitem__(self, i):
        return self.seq[i]
    
    def __add__(self, other):
        return RNA(self.seq + other.seq)

    def complementary_DNA(self):
        forward = self.complementary()
        return DNA(seq=forward)
    
    def __eq__(self, other):
        if self.seq == other.seq:
            return True
        return False
    
    def __repr__(self):
        return self.seq
    
    def __str__(self):
        return str(type(self).__name__) + ": " + self.seq
    
class DNA(NA):
    def __init__(self, seq, seq_reversed=None): 
        self._dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        if self.correct(seq) and self.correct(seq_reversed) == True:
            super().__init__(seq=seq)
        else:
            raise Exception
        super().__init__(seq=seq)
        self.reversed = seq_reversed
        if self.reversed is None:
            self.reversed = self.complementary()

    def __getitem__(self, i):
        return [self.seq[i], self.reversed[i]]
    
    def __add__(self, other):
        return DNA(self.seq + other.seq, self.reversed + other.reversed)
    
    def __eq__(self, other):
        if (self.seq == other.seq) and (self.reversed == other.reversed):
            return True
        return False
    
    def __repr__(self):
        return repr([self.seq, self.rev])
    
    def __str__(self):
        return str(type(self).__name__) + ": " + self.seq + " " + self.complementary()

dna = DNA('ATC', 'TAG')
rna = RNA('GAU')
dna1 = DNA('GC', 'CG')
rna1 = RNA('CU')

print(rna)
print(rna[2], dna[2])

print(dna==dna1)

print(dna.complementary())
print(rna, rna.complementary_DNA())

print(rna + rna1, dna + dna1)

print(rna * rna1)
print(dna*dna1, dna*dna1)




