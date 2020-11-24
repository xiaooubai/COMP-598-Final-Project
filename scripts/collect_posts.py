import requests
import json
import argparse
import math


class IntegerDivision:
    def __init__(self, n, m):
        self.q, self.r = self.euclid_div(n, m)
        self.n = n
        self.m = m

    def __add__(self, other):
        if isinstance(other, int):
            result = self.n + other
            return IntegerDivision(result, self.m)

        result = self.n + other.n
        if self.m != other.m:
            raise ValueError("In order to add 2 IntegerDivision objects, the divider must be the same.")
        return IntegerDivision(result, self.m)

    def __sub__(self, other):
        if isinstance(other, int):
            result = self.n - other
            return IntegerDivision(result, self.m)

        result = self.n - other.n
        if self.m != other.m:
            raise ValueError("In order to substract 2 IntegerDivision objects, the divider must be the same.")
        return IntegerDivision(result, self.m)

    def __lt__(self, other):
        if isinstance(other, int):
            return self.n < other
        return self.n < other.n

    def __gt__(self, other):
        if isinstance(other, int):
            return self.n > other
        return self.n > other.n

    def __call__(self):
        return self.q, self.r

    @staticmethod
    def euclid_div(n, m):
        """
        :param n: original integer to divide
        :param m: integer by which we divide n
        :return: a tuple (q, r) where n = mq+r and r < m
        """
        q = math.floor(n / m)
        r = n % m
        return q, r


def write_posts(subreddit, out_file, loops_remainder, listing):
    """
    :param subreddit: raw name of the subreddit as in the command line argument.
    :param out_file: where to write the posts (in JSON format)
    :param loops_remainder: object of type IntegerDivision that encodes the number of posts (n) and the chunk size (m).
    :param listing: new, hot, rising, etc. Will be passed into the query as an argument
    :return: void
    """

    def loop(after, num_posts):
        if num_posts == 0:  # Reddit has this glitch where, if we pass 0 as "limit", it still returns at least 1 post,
            # so we bypass that if we're at the last iteration (remainder is 0)
            return None

        if after is None:
            raw_data = requests.get(f"http://api.reddit.com{subreddit}/{listing}?limit={num_posts}",
                                    headers={"User-Agent": "windows:requests (by /u/cristian)"})
        else:
            raw_data = requests.get(f"http://api.reddit.com{subreddit}/{listing}?limit={num_posts}&after={after}",
                                    headers={"User-Agent": "windows:requests (by /u/cristian)"})

        data = raw_data.json()
        children = data['data']['children']

        all_posts = []
        for post in children:
            if post['data']['stickied']:
                continue
            else:
                all_posts.append(post['data'])

        effective_num_posts = len(all_posts)
        after = data['data']['after']

        for post in all_posts:
            line = json.dumps(post)
            out_file.write(line)
            out_file.write("\n")

        return after, effective_num_posts

    after_var = None

    while loops_remainder.q > 0:
        m = loops_remainder.m
        (after_var, effective_var) = loop(after_var, m)
        loops_remainder -= effective_var

    while loops_remainder > 0:
        (after_var, effective_var) = loop(after_var, loops_remainder.r)
        loops_remainder -= effective_var


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", type=str, required=True,
                        help="Enter the path to the output file.")
    parser.add_argument("-r", "--subreddit", type=str, required=True,
                        help="Enter the name of the subreddit to fetch the posts from. Ex: /r/politics")
    parser.add_argument("-l", "--listing", type=str, required=True,
                        help="Enter the name of the listing parameter to pass in the query. Ex: new")
    parser.add_argument("-n", "--num_posts", type=int, required=True,
                        help="Enter the number of posts to fetch.")
    args = parser.parse_args()

    out_filename = args.output_file
    subreddit = args.subreddit
    listing = args.listing
    num_posts = args.num_posts

    loops_remainder = IntegerDivision(num_posts, 100)

    with open(out_filename, "w") as f:
        write_posts(subreddit, f, loops_remainder, listing)


if __name__ == "__main__":
    main()
