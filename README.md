# Hyak Demo

## Useful Hyak Commands:

- `hyakalloc`: See available resources (you will see two tables: the first are resources available specific to group(s) you're in, the second are unused resources by groups you're not in, but are available to you anyways, called [checkpoint resources](https://hyak.uw.edu/docs/compute/checkpoint/)).
- `hyakstorage`: Shows your disk usage.
- `dns`: The package manager for Rocky Linux, which Hyak is running. You can do `dns search <script>` to see which package was installed for a certain command. I used this for figuring out which package installed [`sinfo`](https://slurm.schedmd.com/sinfo.html), which shows "information about Slurm nodes and partitions".
- `squeue -u $USER --long`: Shows jobs you're running.
- `sinfo`: Shows information about Slurm nodes and partitions.
- `sacct`: Shows job information (running/stopped/pending/etc..).
- `sacct --starttime <YYYY-MM-DD> --format=User,JobID,Jobname%50,partition,state,time,start,end,elapsed,MaxRss,MaxVMSize,nnodes,ncpus,nodelist`: Shows job history from specified date `<YYYY-MM-DD>` ([source](https://stackoverflow.com/questions/48187625/slurm-job-history-get-full-length-jobname)).
- `scancel <JOBID>`: Cancel a job with ID `<JOBID>`.
- `scp`: Copy files from another computer using SSH.
- `nvidia-smi`: Shows graphics card usage (only works when inside an interactive session with a GPU).
- `ps -lu $USER`: Shows niceness of processes you're running.
- `module avail`: List available modules (only works in compute node)
- `module load <module>`: Load specified module (only works in compute node)
- `module list`: List loaded modules (only works in compute node)

- `salloc -A amath -p ckpt -N 1 -n 2 -c 4 -G 1 --mem=4G --time=5:00:00 --nice=0`
  - `-A amath`: `amath` group (from running the `groups` command).
  - `-p ckpt`: resource patition being used (from `sinfo`, I have access to `gpu-rtx6k` from amath or `ckpt`).
  - `-N 1`: number of nodes these resources spread across (most of the time it's `1`, unless code supports another case).
  - `-n 2`: the maximum number of tasks that is expected to be launched to complete the job.
  - `-c 4`: number of compute cores needed (CPUs per task).
  - `-G 1`: the number of GPUs required for this job.
  - `--mem=4G`: amount of RAM needed.
  - `-t`: maximum runtime for the job (`h:m:s` or `days-hours` or `minutes`).
  - `--nice=<value>`: `<value>` is a number `-2147483645 <= <value> <= 2147483645`, higher nice means the job has a lower priority and can be preempted by a job with a higher priority. Please use higher nice values for jobs that are expected to take longer to run!

## Demo 1: Running Python in CLI

```
$ ssh hyak
$ hyakalloc
$ hyakstorage

$ salloc -A amath -p gpu-rtx6k -N 1 -n 2 -c 2 -G 1 --mem=16G --time=5:00:00 --nice=0
$ squeue -u $USER --long

$ micromamba env list
$ micromamba create --name demo1 python=3.13
$ micromamba activate demo1

$ python --version
$ python -c "print('Hey! '*10)"
```

## Demo 2: Running Python in VSCode

```
https://ondemand.hyak.uw.edu
```

## Demo 3: Running Cursor

* Set up intracluster keys [link](https://hyak.uw.edu/docs/setup/ssh/#intracluster-ssh-keys)
* Create interactive session
* SSH into interactive session [link](https://hyak.uw.edu/docs/hyak101/python/ssh)

```
Host klone-login
  User UWNetID
  Hostname klone.hyak.uw.edu
  ServerAliveInterval 30
  ServerAliveCountMax 1200
  ControlMaster auto
  ControlPersist 3600
  ControlPath ~/.ssh/%r@klone-login:%p

Host klone-node
  User UWNetID
  Hostname n3000
  ProxyJump klone-login
```

## Demo 3: Containers

* Create a container [link](https://hyak.uw.edu/docs/hyak101/python/container/)

```
$ apptainer build apptainer.sif apptainer.def
$ python scripts/generate_slurms.py
$ python scripts/execute_all_slurms.py
```
