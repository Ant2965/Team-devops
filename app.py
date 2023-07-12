import psutil
from flask import Flask, render_template
from prometheus_client import CollectorRegistry, Guage, push_to_gateway
app = Flask(__name__)
registry=CollectorRegistry()
mem=Guage('mem_metric','last time',registry=registry)
cpu=Guage('cpu_metric','last time',registry=registry)
cpu.set_to_current_time()
mem.set_to_current_time()


@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    mem.set(mem_metric)
    cpu.set(cpu_metric)
    push_to_gateway('prom-prometheus-pushgateway:80',job='batchA',registry=registry)

    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)



if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')
###