

#calss header
class _GENERALLY():
	def __init__(self,): 
		self.name = "GENERALLY"
		self.definitions = [u'considering the whole of someone or something, and not just a particular part of him, her, or it: ', u'usually, or in most situations: ', u'by most people, or to most people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
