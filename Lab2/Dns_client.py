import dns.resolver

def dns_demo():
    domain = input("Enter domain [default example.com]: ").strip() or "example.com"
    records = ["A", "MX", "CNAME"]

    with open("dns_output.txt", "w") as out:
        for rtype in records:
            try:
                ans = dns.resolver.resolve(domain, rtype)
                for rec in ans:
                    print(f"{rtype}: {rec}")
                    out.write(f"{rtype}: {rec}\n")
            except Exception:
                print(f"{rtype}: not available")
                out.write(f"{rtype}: not available\n")

if __name__ == "__main__":
    dns_demo()
