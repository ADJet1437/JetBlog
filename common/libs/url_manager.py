from app import db


class UrlManager(object):

    @staticmethod
    def buildUrl(path):
        # TODO: move to conf file
        domain_name = "http://0.0.0.0:5001/"
        return "%s%s" % (domain_name, path)

    @staticmethod
    def buildStaticUrl(path):
        """

        :param path:
        :return:
        """
        path = "/static" + path
        return UrlManager.buildUrl( path )