import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EncounterListMenuComponent } from './encounter-list-menu.component';

describe('EncounterListMenuComponent', () => {
  let component: EncounterListMenuComponent;
  let fixture: ComponentFixture<EncounterListMenuComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EncounterListMenuComponent]
    });
    fixture = TestBed.createComponent(EncounterListMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
