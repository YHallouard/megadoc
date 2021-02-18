Git
===

Rebase a branch on master
#########################

.. code-block:: bash

    # Check that your local master is up-to-date
    git checkout master & git pull
    # Go on you otherBranch
    git checkout otherBranch
    # Rebasing
    git rebase master
    # Push
    git push --force-with-lease

Merging a Branch
#########################

.. code-block:: bash

    # Back on master
    git checkout master
    # Merging
    git merge otherBranch
    # Push
    git push

Delete a Branch
#########################

.. code-block:: bash

    # delete branch locally
    git branch -d localBranchName

    # delete branch remotely
    git push origin -d remoteBranchName

See all branches on remote and local
####################################
.. code-block:: bash

    git branch -avv

Revert a commit
###############
.. code-block:: bash

    git revert HEAD~1..HEAD

or

.. code-block:: bash

    git reset --hard HEAD^

Revert several commits

.. code-block:: bash

    git revert HEAD~3..HEAD

Resolving merge conflicts automatically
#######################################
In cases when you prefer the work of other developers rather than yours.

.. code-block:: bash

    git pull -X theirs

In cases when you prefer your work.

.. code-block:: bash

    git pull -X ours
