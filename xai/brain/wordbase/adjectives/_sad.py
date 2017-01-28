

#calss header
class _SAD():
	def __init__(self,): 
		self.name = "SAD"
		self.definitions = [u'unhappy or sorry: ', u'If something looks sad, it looks worse than it should because it is not being cared for: ', u'not satisfactory or pleasant: ', u'something you say when you are telling someone about something bad that happened: ', u'showing that you are not fashionable or interesting or have no friends: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
