from pathlib import Path

top_dir = Path(__file__).parent.parent

cmd_template = \
"""\
#!/bin/bash

#SBATCH --account=amath
#SBATCH --partition=gpu-rtx6k
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus=1
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-0:10
#SBATCH --nice=0

#SBATCH --job-name=job_{id}
#SBATCH --output=/mmfs1/home/alexeyy/storage/demo/logs/job_{id}_%j.out

#SBATCH --mail-type=NONE
#SBATCH --mail-user=alexeyy@uw.edu

demo_dir="/mmfs1/home/alexeyy/storage/demo"

echo "Running Apptainer"

apptainer run --nv --bind "$demo_dir":/app/demo "$demo_dir"/containers/apptainer.sif python /app/demo/scripts/make_file.py --id {id} --out_dir /app/demo/out

echo "Finished running Apptainer"\
"""

# Clean up slurm repo
slurm_dir = top_dir / 'slurms'
for file in slurm_dir.glob('*.slurm'):
    file.unlink()

for id in range(2):
    cmd = cmd_template.format(
        id=id
    )

    with open(top_dir / 'slurms' / f'{id}.slurm', "w") as f:
        f.write(cmd)
