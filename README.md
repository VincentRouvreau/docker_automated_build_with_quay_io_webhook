# How to build docker images in a CI workflow using quay.io webhooks

As docker is now well integrated to most CI providers, docker images with all
your dependencies already installed can help you to save installation time on
your CI workflows.

But the tools to trigger docker image build are not always well integrated to
services like github.

The idea of this tutorial is to show you how to trigger docker image build
only when it is necessary:

![triggers](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/VincentRouvreau/docker_automated_build_with_quay_io_webhook/main/uml/triggers.iuml)

## Code sample

our code is quite simple and easy, it is a python package called `sample`.
It is composed of a single function called `determinant` that returns the
determinant of a given matrix as input.
This function is using the determinant function from
[numpy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html).

numpy is one of our dependencies as described in
[requirements.txt](requirements.txt).

pytest is our second dependency for the unitary tests to be run. As this is
more a test dependency, it could be located in a test-requirements.txt for
example.

## Dockerfile

A first approach would be to install dependencies as described here:
```docker
FROM python:3.7-alpine

# required for numpy
RUN apk add g++

# 1st solution
RUN pip install numpy pytest
```

This solution is not really [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

A better approach would be to install dependencies from the requirements.txt:

```
FROM python:3.7-alpine

# required for numpy
RUN apk add g++

# 2nd solution
COPY requirements.txt /
RUN pip install -r /requirements.txt
```

Now, the question is how to build the docker image when Dockerfile and/or
requirements.txt change ?

## quay.io webhooks

*Note that this section is copied from
[automated-quay.io-deployment](https://github.com/lkiesow/automated-quay.io-deployment/).*

*Note that this will work for public repositories only.*

Go to the "Builds" section in your repository on quay.io and select
"Create Build Trigger" and "Custom Git Repository Push".
In the following dialog, use the HTTPS variant for your Github repository URL.
That makes it completely unnecessary to deal with any SSH keys later on.

After it has been successfully created, you will get a Webhook Endpoint URL
which you will need for GitHub actions. The URL should look somewhat like this:

```
https://$token:...@quay.io/webhooks/push/trigger/...
```

## Setting up GitHub action

In your GitHub project settings, add a repository secrets called
`QUAY_WEBHOOK_URL` with the value of the previous URL.

Now you can have a look to
[docker_build.yml](.github/workflows/docker_build.yml)
to see how the webhook is triggered and see that it will be only `on`
Dockerfile and/or requirements.txt `push`.

The other GitHub action will just have to use the docker image (that will be up
to date thanks to the `docker_build` GitHub action) and to launch `pytest`.
