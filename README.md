# Wrapper for AWS Batch use at Fred Hutch

This wrapper enables secure use of AWS Batch
at Fred Hutch and works around some
[security issues](https://forums.aws.amazon.com/thread.jspa?threadID=270071&tstart=0)
related to submission and termination of jobs.

For the most part, you use AWS Batch as you normally would, as explained in its
[documentation](https://aws.amazon.com/documentation/batch/)
and the [Fred Hutch Batch documentation](https://fredhutch.github.io/aws-batch-at-hutch-docs/).

The only difference (explained below) is when you want to submit a job,
or terminate/cancel a job.

## Installation

First, use a version of Python 3:

```
ml Python/3.6.4-foss-2016b-fh1
```

Now, install the package:

```
pip install fredhutch_batch_wrapper --user
```

(If you are using a [virtual environment](https://docs.python.org/3/tutorial/venv.html),
you can omit the `--user`).

Check to see if the executable is in your path:

```
which batchwrapper
```

If this returns nothing, then make sure that the
directory `$HOME/.local/bin` is in your `PATH`
by editing the file `~/.bash_profile` and adding this
line at the end:

```
export PATH=$PATH:$HOME/.local/bin
```

To make this take effect right away (without having
to log out and back in again), source the file:

```
source $HOME/.bash_profile
```

Now, `which batchwrapper` should return the path
to the `batchwrapper` executable.

### AWS Credentials

If you haven't already, please [obtain your AWS credentials](https://teams.fhcrc.org/sites/citwiki/SciComp/Pages/Getting%20AWS%20Credentials.aspx) and
[request access](https://fredhutch.github.io/aws-batch-at-hutch-docs/#request-access) to AWS Batch before proceeding further.
AWS credentials (and Batch onboarding) are required before this
Batch wrapper will work.

## Usage

There are two ways to use this wrapper: via the command line,
and via Python. (Soon you will be able to submit and terminate
jobs via the [batch dashboard](https://batch-dashboard.fhcrc.org/)).

### Command Line

Usage is similar to that of the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/batch/index.html) for Batch.

In fact, you should continue to use the CLI for everything except
submitting jobs (`submit-job`), terminating jobs (`terminate-job`),
and canceling jobs (`cancel-job`).

Running the `batchwrapper` command without any arguments gives brief help:

```
usage: batchwrapper [-h] {submit,cancel,terminate} ...

Wrapper for submitting/terminating AWS Batch jobs.

Type

batchwrapper <subcommand> --help

for help on each subcommand.

positional arguments:
  {submit,cancel,terminate}
                        sub-command help
    submit              submit a job
    cancel              cancel a job
    terminate           terminate a job

optional arguments:
  -h, --help            show this help message and exit
```

#### Submitting a job

You can get some help with `batchwrapper submit -h`:

```
usage: batchwrapper submit [-h] --cli-input-json JSONFILE

optional arguments:
  -h, --help            show this help message and exit
  --cli-input-json JSONFILE
                        provide name of a JSON file containing arguments
```

To submit a job, you need to put the pertinent information in a JSON file.
Unlike with the AWS CLI, you don't put the `file://` prefix in front of the
JSON file.

You can prepare a json file by following the
[example](https://fredhutch.github.io/aws-batch-at-hutch-docs/#submit-your-job) in the Fred Hutch batch documentation.

Assuming your JSON file is called `job.json`, you can submit it
as follows:

```
batchwrapper submit --cli-input-json job.json
```

The batch wrapper will return the Job ID and name.

#### Terminating a job

Brief help is available with `batchwrapper terminate -h`:

```
usage: batchwrapper terminate [-h] --job-id JOB_ID --reason REASON

optional arguments:
  -h, --help       show this help message and exit
  --job-id JOB_ID  job ID
  --reason REASON  reason for terminating job
```

So, for example, you can terminate a job you own with the following
command (replace the job ID with your own):


```
batchwrapper terminate --job-id 13732097-3f5d-42bc-b60f-2cd166486074 \
   --reason "there is a problem"
```

#### Canceling a job

Brief help is available with `batchwrapper cancel -h`:

```
usage: batchwrapper cancel [-h] --job-id JOB_ID --reason REASON

optional arguments:
  -h, --help       show this help message and exit
  --job-id JOB_ID  job ID
  --reason REASON  reason for canceling job
  ```

So, for example, you can cancel a job you own with the following
command (replace the job ID with your own):



```
batchwrapper cancel --job-id 13732097-3f5d-42bc-b60f-2cd166486074 \
   --reason "there is a problem"
```

### Within Python

Using the wrapper in Python is very similar to using the
[batch client](https://boto3.readthedocs.io/en/latest/reference/services/batch.html#client)
in `boto3`. In fact, you will continue to use `boto3` for everything
except submitting, terminating, and canceling jobs.

In order to use the wrapper, you must first create a client:

```python
import fredhutch_batch_wrapper

client = fredhutch_batch_wrapper.get_client()
```

The `client` object has three methods: `submit_job()`, `cancel_job()`,
and `terminate_job()`. They take exactly the same arguments
(and return the same values)
as their
counterparts in `boto3`:

* [submit_job()](https://boto3.readthedocs.io/en/latest/reference/services/batch.html#Batch.Client.submit_job)
* [cancel_job()](https://boto3.readthedocs.io/en/latest/reference/services/batch.html#Batch.Client.cancel_job)
* [terminate_job()](https://boto3.readthedocs.io/en/latest/reference/services/batch.html#Batch.Client.terminate_job)

## More Information

* [AWS CLI Batch Documentation](https://docs.aws.amazon.com/cli/latest/reference/batch/index.html)
* [boto3 Batch Documentation](https://boto3.readthedocs.io/en/latest/reference/services/batch.html#client)
* [Using AWS Batch at Fred Hutch](https://fredhutch.github.io/aws-batch-at-hutch-docs/)
* [Getting AWS Credentials](https://teams.fhcrc.org/sites/citwiki/SciComp/Pages/Getting%20AWS%20Credentials.aspx)

If you have further questions, please contact
[SciComp](https://centernet.fredhutch.org/cn/u/center-it/cio/scicomp.html).
