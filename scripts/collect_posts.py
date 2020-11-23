import requests
import json
import argparse
import math


def write_posts(subreddit, out_file, remainder, times, listing):
    """
    :param subreddit: raw name of the subreddit as in the command line argument.
    :param out_file: where to write the posts (in JSON format)
    :param remainder: number of posts % 100. This and the next parameter are there because of the API limitation
    to only output at most 100 posts at a time.
    :param times: biggest multiple of 100 less than or equal to the number of posts
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
        not_stickied_posts = [post['data'] for post in children if not post['data']['stickied']]
        after = data['data']['after']

        for post in not_stickied_posts:
            line = json.dumps(post)
            out_file.write(line)
            out_file.write("\n")

        return after

    after_var = None
    for i in range(times + 1):
        if i == times:
            _ = loop(after_var, remainder)
        else:
            after_var = loop(after_var, 100)


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
    multiples_of_100 = math.floor(num_posts / 100)
    remainder_division_by_100 = num_posts % 100

    with open(out_filename, "w") as f:
        write_posts(subreddit, f, remainder_division_by_100, multiples_of_100, listing)


if __name__ == "__main__":
    main()
