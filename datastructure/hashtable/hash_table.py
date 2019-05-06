# Open Addressing
class OpenAddressingHashTable:
    SIZE = 1000;
     
    private String[] hashtable = new String[SIZE];
    
    def insert(self, value:string):
        probe = 0
    # public void add(String value) {
        int probe = 0;
        while probe < SIZE:
            
        do {
            int hash = hash(value, probe);
            if (hashtable[hash] == null) {
                hashtable[hash] = value;
                return;
            }
            probe++;
        } while (probe < SIZE);
 
        // hash table is full
        throw new RuntimeException("Hash table overflow");
    }
 
    public boolean contains(String value) {
        int probe = 0;
 
        do {
            int hash = hash(value, probe);
            if (hashtable[hash] == null) {
                return false;
            } else {
                if (hashtable[hash].equals(value)) {
                    return true;
                }
                probe++;
            }
 
        } while (probe < SIZE);
 
        return false;
    }
 
    private int hash(String value, int probe) {
        HashFunction hf = Hashing.murmur3_128(); // can choose any hash function
        int hash = Math.abs(hf.newHasher().putString(value, Charsets.UTF_8).hash().asInt()) % SIZE;
 
        return (hash + probe) % SIZE;
    }
 

# Tombstone