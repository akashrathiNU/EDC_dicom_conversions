import os
import glob
import sys

#Setting input arguments as variables
sub = sys.argv[1]
ses = sys.argv[2]



# Make anatomical, functional, dwi, and fieldmap folders in bids folder
def make_bids_dirs(sub,ses,bids_dir):
    anat_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'anat/'
    os.makedirs(anat_dir, exist_ok=True)

    func_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'func/'
    os.makedirs(func_dir, exist_ok=True)

    fmap_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'fmap/'
    os.makedirs(fmap_dir, exist_ok=True)
   
    fmap_dir = bids_dir+'/'+'sub-'+sub+'/'+ses+'/'+'dwi/'
    os.makedirs(fmap_dir, exist_ok=True)

# Rename each filename to BIDS format
def rename_partic(sub, ses, bids_dir): 
    print(sub + " " + bids_dir)
    print("in rename partic")
    directory = bids_dir+'/sub-'+sub+'/'+ses+'/'
    print(directory)

    


    # MID1
    files = sorted(glob.glob(directory + "*--MID1_2p4_ME5-*e1*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_echo-1_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID1_2p4_ME5-*e2*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_echo-2_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 
        
    files = sorted(glob.glob(directory + "*--MID1_2p4_ME5-*e3*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_echo-3_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID1_2p4_ME5-*e4*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_echo-4_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID1_2p4_ME5-*e5*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-01_echo-5_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    #MID2
    files = sorted(glob.glob(directory + "*--MID2_2p4_ME5-*e1*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_echo-1_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID2_2p4_ME5-*e2*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_echo-2_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 
        
    files = sorted(glob.glob(directory + "*--MID2_2p4_ME5-*e3*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_echo-3_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID2_2p4_ME5-*e4*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_echo-4_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--MID2_2p4_ME5-*e5*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-mid_run-02_echo-5_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    # NBACK1
    files = sorted(glob.glob(directory + "*--NBACK1_2p4_ME5-*e1*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-01_echo-1_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK1_2p4_ME5-*e2*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-01_echo-2_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 
        
    files = sorted(glob.glob(directory + "*--NBACK1_2p4_ME5-*e3*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-01_echo-3_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK1_2p4_ME5-*e4*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-01_echo-4_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK1_2p4_ME5-*e5*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-01_echo-5_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    # NBACK2
    files = sorted(glob.glob(directory + "*--NBACK2_2p4_ME5-*e1*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-02_echo-1_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK2_2p4_ME5-*e2*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-02_echo-2_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 
        
    files = sorted(glob.glob(directory + "*--NBACK2_2p4_ME5-*e3*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-02_echo-3_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK2_2p4_ME5-*e4*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-02_echo-4_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name) 

    files = sorted(glob.glob(directory + "*--NBACK2_2p4_ME5-*e5*"), key=str)
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_task-nback_run-02_echo-5_bold." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

    #T1w image
    counter = 0
    files = glob.glob(directory + "*MPRAGE*")
    for file in files:
        if counter < 2:
            print(file)
            parts = file.split(".", 1)
            new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_T1w." + parts[1])
            print(directory + new_name)
            os.rename(file, new_name)
            counter +=1   
        else: 
            print(file)
            parts = file.split(".", 1)
            new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-2_T1w." + parts[1])
            print(directory + new_name)
            os.rename(file, new_name)
            counter +=1

    #DWI AP
    files = glob.glob(directory + "*DTI_AP*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_dir-AP_dwi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

    #DWI PA
    files = glob.glob(directory + "*DTI_PA*")
    for file in files:
        print(file)
        parts = file.split(".", 1)
        new_name = os.path.join(directory,"sub-" + sub + "_" + ses + "_run-1_dir-PA_dwi." + parts[1])
        print(directory + new_name)
        os.rename(file, new_name)

def main(sub, ses, bids_dir='/Users/akashrathi/Documents/Github/EDC_dicom_conversions/bids'):
    make_bids_dirs(sub,ses,bids_dir)
    rename_partic(sub,ses,bids_dir)

main(sub, ses)
