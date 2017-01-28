

#calss header
class _GENERAL():
	def __init__(self,): 
		self.name = "GENERAL"
		self.definitions = [u'involving or relating to most or all people, things, or places, especially when these are considered as a unit: ', u'usually, or in most situations: ', u'considering the whole of someone or something, and not just a particular part of him, her, or it: ', u'to be a good thing for the public: ', u'not detailed, but including the most basic or necessary information: ', u'things considered as a unit and without giving attention to details: ', u'including a lot of things or subjects and not limited to only one or a few: ', u'used as part of the title of a job of someone who is in charge of a whole organization or company: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
