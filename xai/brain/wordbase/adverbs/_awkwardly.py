

#calss header
class _AWKWARDLY():
	def __init__(self,): 
		self.name = "AWKWARDLY"
		self.definitions = [u'in a worried or embarrassed way: ', u'in an embarrassing or worrying way, or a way that causes problems: ', u'moving in a way that is not natural, relaxed, or attractive: ', u'in a way that is difficult to deal with, use, or do: ', u'in an intentionally unhelpful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
