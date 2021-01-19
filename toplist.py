class Record:
    def __init__(self, tx, addr, type, amount, node, time):
        self.tx = tx
        self.addr = addr
        self.type = type
        self.amount = float(amount) / 1e9
        self.node = node
        self.time = time


if __name__ == "__main__":
    records = []
    for file in [
            "./00-block-1-341029.csv",
            "./01-block-341030-528252.csv",
            "./02-block-528253-916600.csv",
            "./03-block-916601-1107709.csv",
            "./04-block-1107710-4329470.csv",
            "./05-block-4329471-7466895.csv",
            "./06-block-7466896-8427516.csv",
    ]:
        with open(file, "r") as f:
            for line in f:
                lp = [t.strip() for t in line.split(',')]
                if len(lp) != 7 or len(lp[1]) == 0 or lp[1][:2] != "P-":
                    continue
                records.append(Record(*lp[:-1]))
    rewards = {}
    for rec in records:
        rw = rewards[rec.addr] = rewards.get(rec.addr, {
            'total': 0,
            'staking': 0,
            'delegator': 0,
            'delegatee': 0
        })
        rw['total'] += rec.amount
        rw[rec.type] += rec.amount
    sorted = []
    for (addr, d) in rewards.items():
        sorted.append((addr, d['total']))
    sorted.sort(reverse=True, key=lambda x: x[1])
    print("Top total rewards,")
    for d in sorted[:100]:
        print("{},{}".format(d[0], d[1]))
    sorted.clear()
    nodes = {}
    for rec in records:
        if rec.type == "delegator":
            rw = nodes[rec.node] = nodes.get(rec.node, {
                'count': 0,
                'amount': 0,
            })
            rw['count'] += 1
            rw['amount'] += rec.amount
    for (node, d) in nodes.items():
        sorted.append((node, d['count']))
    sorted.sort(reverse=True, key=lambda x: x[1])
    print("Popular nodes by delegators,")
    for d in sorted[:100]:
        print("{},{}".format(d[0], d[1]))
    sorted.clear()
    for (node, d) in nodes.items():
        sorted.append((node, d['amount']))
    sorted.sort(reverse=True, key=lambda x: x[1])
    print("Popular nodes by delegation amount,")
    for d in sorted[:100]:
        print("{},{}".format(d[0], d[1]))
    sorted.clear()
