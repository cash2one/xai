

#calss header
class _POSTAL():
	def __init__(self,): 
		self.name = "POSTAL"
		self.definitions = [u'relating to post or to the public service that collects and delivers the post: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
