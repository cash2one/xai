

#calss header
class _HOT():
	def __init__(self,): 
		self.name = "HOT"
		self.definitions = [u'having a high temperature: ', u'used to describe food that causes a burning feeling in the mouth: ', u'used to describe a subject that causes a lot of disagreement or discussion: ', u'new and exciting: ', u'knowing a lot or skilful: ', u'an accurate piece of advice about who will win a race: ', u'the person or animal that is most likely to win a race, competition, election, etc.: ', u'to think that a particular thing is very important and to demand that it is done well or correctly: ', u'Hot goods have been recently stolen and are therefore difficult to sell or dangerous to deal with because the police are still looking for them.', u'sexually attractive, or feeling sexually excited: ', u'If someone has a hot temper, they are easily made angry.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
