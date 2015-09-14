#!/usr/bin/python
# -*- coding: utf-8 -*-


class Forums(object):
    """
    Contains logic for the Sakai Forums tool.

    More information about the RESTful interface can be found at:
    https://sakai.rutgers.edu/direct/forums/describe
    """
    def __init__(self, rq):
        """
        Create a standalone Forums Object
        :param rq: The RequestHandler to use.
        :return: A Forums object
        """
        self.requester = rq

    def getForumsForSite(self, siteid):
        """
        Get all of the forums for the specified site.
        :param siteid: The ID of the site.
        :return: A JSON representation of the forums for the specified site.
        """
        return self.requester.executeRequest('/direct/forums/site/{0}.json'.format(siteid))

    def getAllTopicsForForum(self, siteid, forumid):
        """
        Get all of the topics for the specified forum within the specified site.
        :param siteid: The ID of the site.
        :param forumid: The ID of the forum.
        :return: A JSON representation of the topics for the given forum within the given site.
        """
        return self.requester.executeRequest('/direct/forums/site/{0}/forum/{1}.json'.format(siteid,
                                                                                             forumid))

    def getAllConversationsForTopic(
            self,
            siteid,
            forumid,
            topicid,
    ):
        """
        Get all of the conversations for the given topic within the given topic.
        :param siteid: The ID of the site.
        :param forumid: The ID of the forum.
        :param topicid: the ID of the topic
        :return: A JSON representation of the conversations for the given topic within the given forum in the given site.
        """
        return self.requester.executeRequest('/direct/forums/site/{0}/forum/{1}/topic/{2}.json'.format(siteid,
                                                                                                       forumid,
                                                                                                       topicid))

    def getAllMessagesForConversation(
            self,
            siteid,
            forumid,
            topicid,
            messageid,
    ):
        """
        Get all of the messages for .....you get the idea.
        :param siteid: The ID of the site.
        :param forumid: The ID of the forum.
        :param topicid: the ID of the topic
        :param messageid: The ID of the conversation.
        :return: You get the idea....
        """
        return self.requester.executeRequest(
            '/direct/forums/site/{0}/forum/{1}/topic/{2}/message/{3}.json'.format(siteid,
                                                                                  forumid, topicid, messageid))
