mock --resultdir . --buildsrpm --spec docker-flannel-glue.spec --sources .

mock --resultdir . docker-flannel-glue-0.1-1.src.rpm

yum install docker-flannel-glue-0.1-1.noarch.rpm

Now you can systemctl start docker without having to first start
flanneld, and without having to change any docker configuration to use
flannel.

Note: flannel still needs to be bootstrapped with an etcd endpoint and
its config needs to be stored within etcd.
