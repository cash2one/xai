

#calss header
class _SILHOUETTED():
	def __init__(self,): 
		self.name = "SILHOUETTED"
		self.definitions = [u'forming a silhouette: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
