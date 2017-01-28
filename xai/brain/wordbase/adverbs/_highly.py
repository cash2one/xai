

#calss header
class _HIGHLY():
	def __init__(self,): 
		self.name = "HIGHLY"
		self.definitions = [u'very, to a large degree, or at a high level: ', u'to admire or say admiring things about someone: ', u'in an important or influential (= having a lot of influence) position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
