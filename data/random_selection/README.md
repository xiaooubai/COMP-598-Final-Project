## The tsv formatted posts that were randomly selected from the merged directory
Topics we have so far:

1. cabinet: Mentions the cabinet choice (of Biden).

2. economy\_climate: Any mention to the economy or climate. I chose to put these together in a single topic because they're very intertwined especially in the context of the 2020 election, as climate change is a pressing issue and the main resistence arguments are economical.

3. lawsuit: Any mention about legal challenges, vote fraud and disputes, etc.

4. covid: Mention about the coronavirus.

5. transition: Any post making a reference to the process of transitioning from Biden to Trump or its consequences, whether it's positive or negative.

6. dissatisfaction: Any form of condemnation or negative critique from one side about another.

7. vote: Any mention to vote counts, candidate certification or allusion to support for one candidate or another and that is not tied to the legal problems (see lawsuit).

8. racism: Post references hate speech, white supremacy, or any other topic about racism. 
---
### Coding rules

1. If topic A and topic B both seem to apply to a given post, and one of them is more specific than the other, then assign the most specific topic to the post.

2. If topic A and topic B both seem to apply to a given post and that none of them is a more specific version of the other, then try to find a third topic C that includes A and B, and assign C to the post.

#### Examples

1. "From the coronavirus to the environment, Biden plans to take government in new direction". Possible topics: `covid` and `environment`.
However, they conflict since `covid` is not a specific case of `environment` and `environment` is not a specific case of `covid`.
Hence we find a third topic `transition` which is relevant to the post since it includes `covid` and `environment`.

2. "Biden's Treasury Secretary: Janet Yellen". Possible topics: `cabinet` and `transition`. 
However, `cabinet` is a more specific version of `transition`, so we should assign `cabinet` to the post.

