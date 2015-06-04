class tower():
    #self.id = id
    
    def __init__(self, i):
        self.disks = []
        self.id  = i
    def add_disk(self, disk_id):
        self.disks.append(disk_id)
        
    def moveTop_to(self, desti):
        a = self.disks.pop()
        desti.disks.append(a)
        print 'move disk %s from %s to %s' % (a, self.id, desti.id)
        
def moveDisks(n, init, desti, buffer):
    if n>0:
        moveDisks(n-1, init, buffer, desti)
        init.moveTop_to(desti)
        moveDisks(n-1, buffer, desti, init)
    
def main():
    #if len(towers) != len(final_confg):
    #    print 'error: number of towers doesn't match ...'
    #    return None
    #else:
    
    towers = []
    total_num_disk = 4
    for i in range(3):
        tower_i = tower(i)
        print 'tower', i
        if i == 0:
            for j in range(total_num_disk, 0 , -1):
               tower_i.add_disk(j)
        towers.append(tower_i)
        
    moveDisks(total_num_disk, towers[0], towers[2], towers[1])
    print towers[2].disks
    
if __name__ =='__main__':
    main()
    #final_confg = []
    #assert len(towers) == len(final_confg)
    #
    #    
    #for j in range(total_num_disk):
    #    move()
    
    #move(towers, [[], [2,4],[1,3]])      
    

        
    
    


