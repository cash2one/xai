

#calss header
class _ARYAN():
	def __init__(self,): 
		self.name = "ARYAN"
		self.definitions = [u'relating to white people from northern Europe, especially those with pale hair and blue eyes, who were believed by the Nazis to be better than members of all other races']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
