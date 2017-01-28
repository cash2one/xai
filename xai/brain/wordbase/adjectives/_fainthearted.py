

#calss header
class _FAINTHEARTED():
	def __init__(self,): 
		self.name = "FAINTHEARTED"
		self.definitions = [u'Someone who is fainthearted is not confident or brave and dislikes taking unnecessary risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
