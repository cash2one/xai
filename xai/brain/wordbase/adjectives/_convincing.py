

#calss header
class _CONVINCING():
	def __init__(self,): 
		self.name = "CONVINCING"
		self.definitions = [u'able to make you believe that something is true or right: ', u'a victory in which the person or team that wins is much better than the person or team they are competing against: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
