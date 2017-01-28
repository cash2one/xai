

#calss header
class _RELIABLE():
	def __init__(self,): 
		self.name = "RELIABLE"
		self.definitions = [u'Someone or something that is reliable can be trusted or believed because he, she, or it works or behaves well in the way you expect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
