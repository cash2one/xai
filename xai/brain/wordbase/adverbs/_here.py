

#calss header
class _HERE():
	def __init__(self,): 
		self.name = "HERE"
		self.definitions = [u'in, at, or to this place: ', u'used at the beginning of a statement to introduce someone or something: ', u'used to show that someone has arrived or that something has started: ', u'used to say that someone or something that is near you: ', u'now: ', u'used when giving something to someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
