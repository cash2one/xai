

#calss header
class _SHAMELESS():
	def __init__(self,): 
		self.name = "SHAMELESS"
		self.definitions = [u'not ashamed, especially about something generally considered unacceptable: ', u'behaving in a way intended to attract sexual interest, without feeling ashamed about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
