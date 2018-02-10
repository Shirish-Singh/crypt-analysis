import { ExtendedData } from './extendedData';

export class TweetData {
    text: string;
    extended_tweet: ExtendedData;
    created_at: string;
    reply_count: number;
    retweet_count: string;
    favorite_count: string;
    lang: string;
    // entities: string;
}
