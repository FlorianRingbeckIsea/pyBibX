from . import pbx
from . import helpers

# Function: Get Counts
def __get_counts(self, u_ent, ent, acc = []):
    counts = []
    for i in range(0, len(u_ent)):
        ents = 0
        for j in range(0, len(ent)):
            if (u_ent[i] in ent[j] and len(acc) == 0):
                ents = ents + 1
            elif (u_ent[i] in ent[j] and len(acc) > 0):
                ents = ents + acc[j]
        counts.append(ents)
    return counts

def __total_and_self_citations(self):
    t_c = []
    s_c = []
    for researcher in self.u_aut:
        doc = []
        cit = 0
        i1  = 0
        i2  = 0
        for researchers in self.aut:
            if (researcher in researchers):
                doc.append(self.citation[i1])
                for reference in self.ref[i2]:
                    if (researcher in reference.lower()):
                        cit = cit + 1
            i1 = i1 + 1
        i2 = i2 + 1
        t_c.append(sum(doc))
        s_c.append(cit)
    return t_c, s_c

# Function: Hirsch Index
def __h_index(self):
    h_i = []
    for researcher in self.u_aut:
        doc = []
        i   = 0
        for researchers in self.aut:
            if (researcher in researchers):
                doc.append(self.citation[i])
            i = i + 1
        for j in range(len(doc)-1, -1, -1):
            count = len([element for element in doc if element >= j])
            if (count >= j):
                h_i.append(j)
                break
    return h_i

# Test function for module  
def _test():
    file_name = 'savedrecs_dev.bib'
    database  = 'wos'
    bibfile   = pbx_probe(file_bib = file_name, db = database, del_duplicated = True)

if __name__ == '__main__':
    _test()


