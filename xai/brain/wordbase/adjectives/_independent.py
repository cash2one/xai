

#calss header
class _INDEPENDENT():
	def __init__(self,): 
		self.name = "INDEPENDENT"
		self.definitions = [u'not influenced or controlled in any way by other people, events, or things: ', u'An independent politician does not agree or vote with any particular political party.', u'An independent country is not governed or ruled by another country: ', u'not taking help or money from other people: ', u'An independent grammatical clause forms part of a sentence but can also form a separate sentence.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
