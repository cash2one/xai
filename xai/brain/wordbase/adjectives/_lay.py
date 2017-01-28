

#calss header
class _LAY():
	def __init__(self,): 
		self.name = "LAY"
		self.definitions = [u'not trained in or not having a detailed knowledge of a particular subject: ', u'having a position in a religious organization that is not a full-time job and is not paid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
