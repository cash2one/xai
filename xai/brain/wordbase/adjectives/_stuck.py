

#calss header
class _STUCK():
	def __init__(self,): 
		self.name = "STUCK"
		self.definitions = [u'unable to move, or set in a particular position, place, or way of thinking: ', u'in a difficult situation, or unable to change or get away from a situation: ', u'not able to continue reading, answering questions, etc. because something is too difficult: ', u'to have to deal with someone or something unpleasant because you have no choice or because no one else wants to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
